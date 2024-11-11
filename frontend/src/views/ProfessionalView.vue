<script setup>
import {ref, onMounted} from 'vue';
import {useRoute} from 'vue-router';
import PageContainer from "@/components/PageContainer.vue";
import {updateProfessional, getProfessional} from "@/services/api.js";

const route = useRoute();
const professionalId = route.params.id;

const document = ref('');
const firstName = ref('');
const lastName = ref('');
const email = ref('');


const fetchProfessional = async () => {
  try {
    const professional = await getProfessional(professionalId);
    document.value = professional.document;
    firstName.value = professional.first_name;
    lastName.value = professional.last_name;
    email.value = professional.email;
  } catch (error) {
    alert('Error al cargar los datos del profesional');
  }
};

onMounted(() => {
  fetchProfessional();
});

const handleSubmit = async () => {
  if (!document.value || !firstName.value || !lastName.value || !email.value) {
    alert('Por favor, llene todos los campos');
    return;
  }

  const professionalData = {
    document: document.value,
    first_name: firstName.value,
    last_name: lastName.value,
    email: email.value,
  };

  try {
    await updateProfessional(professionalId, professionalData);
    alert('Profesional actualizado correctamente');
  } catch (error) {
    const errorData = error?.response?.data;

    if (!errorData) {
      alert('Error al actualizar el profesional');
      return;
    }

    const errorMessages = Object.values(errorData).join('\n');
    alert(errorMessages);
  }
};
</script>

<template>
  <PageContainer>
    <div class="nuevo-profesional">
      <h1>SGTH</h1>
      <form class="form-control" @submit.prevent="handleSubmit">
        <h2>Datos personales</h2>
        <div class="form-group">
          <input placeholder="Número de cédula" class="input" type="number" v-model="document"/>
          <input placeholder="Nombre" class="input" v-model="firstName"/>
          <input placeholder="Apellido" class="input" v-model="lastName"/>
          <input placeholder="Correo" class="input" type="email" v-model="email"/>
        </div>
        <div class="buttons-container">
          <router-link to="/profesionales">
            <button class="btn btn-secondary" type="button">Volver</button>
          </router-link>
          <button class="btn btn-primary" type="submit">Guardar Cambios</button>
          <router-link to="/">
            <button class="btn btn-secondary" type="button" @click="resetForm">Salir</button>
          </router-link>
        </div>
      </form>
    </div>
  </PageContainer>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/main.scss";

.nuevo-profesional {
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
