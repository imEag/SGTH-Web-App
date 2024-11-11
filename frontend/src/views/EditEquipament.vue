<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import PageContainer from "@/components/PageContainer.vue";
import { updateDevice, getAllProfessionals, getDevice } from "@/services/api.js";

const route = useRoute();
const deviceId = route.params.id;

const name = ref('');
const brand = ref('');
const area = ref('');
const serial = ref('');
const responsible = ref('');
const professionals = ref([]);

const fetchDevice = async () => {
  try {
    const device = await getDevice(deviceId);
    name.value = device.name;
    brand.value = device.brand;
    area.value = device.area;
    serial.value = device.serial;
    responsible.value = device.responsible;
  } catch (error) {
    alert('Error al cargar los datos del equipo');
  }
};

const fetchProfessionals = async () => {
  try {
    const response = await getAllProfessionals();
    professionals.value = response.data;
  } catch (error) {
    alert('Error al cargar la lista de profesionales');
  }
};

onMounted(() => {
  fetchDevice();
  fetchProfessionals();
});

const handleSubmit = async () => {
  if (!name.value || !brand.value || !area.value || !serial.value || !responsible.value) {
    alert('Por favor, llene todos los campos');
    return;
  }

  const deviceData = {
    name: name.value,
    brand: brand.value,
    area: area.value,
    serial: serial.value,
    responsible: responsible.value,
  };

  try {
    await updateDevice(deviceId, deviceData);
    alert('Equipo actualizado correctamente');
  } catch (error) {
    const errorData = error?.response?.data;
    if (!errorData) {
      alert('Error al actualizar el equipo');
      return;
    }
    const errorMessages = Object.values(errorData).join('\n');
    alert(errorMessages);
  }
};
</script>

<template>
  <PageContainer>
    <div class="nuevo-equipo">
      <h1>Actualizar Equipo</h1>
      <form class="form-control" @submit.prevent="handleSubmit">
        <h2>Datos del Equipo</h2>
        <div class="form-group">
          <input placeholder="Nombre del equipo" class="input" v-model="name" />
          <input placeholder="Marca" class="input" v-model="brand" />
          <input placeholder="Área" class="input" v-model="area" />
          <input placeholder="Número de serie" class="input" v-model="serial" />
          <select class="input" v-model="responsible">
            <option disabled value="">Seleccione el responsable</option>
            <option v-for="prof in professionals" :key="prof.id" :value="prof.id">
              {{ prof.first_name }} {{ prof.last_name }}
            </option>
          </select>
        </div>
        <div class="buttons-container">
          <router-link to="/devices-list">
            <button class="btn btn-secondary" type="button">Volver</button>
          </router-link>
          <button class="btn btn-primary" type="submit">Guardar Cambios</button>
          <router-link to="/">
            <button class="btn btn-secondary" type="button">Salir</button>
          </router-link>
        </div>
      </form>
    </div>
  </PageContainer>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/main.scss";

.nuevo-equipo {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: $questrial;
  text-align: center;

  h1 {
    margin-bottom: 10px;
  }

  .form-group {
    display: flex;
    gap: 70px;
    justify-content: center;
    margin: 20px;
  }

  .buttons-container {
    display: flex;
    gap: 70px;
    justify-content: center;
    margin-top: 100px;
  }

  .input {
    padding: 10px;
    border-radius: 15px;
    border: 1px solid #ccc;
    width: 200px;
  }

  .btn-primary {
    background-color: #00bcd4;
    color: black;
    padding: 10px 20px;
    border-radius: 15px;
    border: none;
    cursor: pointer;
  }

  .btn-secondary {
    background-color: #e0e0e0;
    color: black;
    padding: 10px 20px;
    border-radius: 15px;
    border: none;
    cursor: pointer;
  }
}
</style>
