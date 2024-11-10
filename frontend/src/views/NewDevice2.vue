<script setup>
import {ref} from 'vue';
import PageContainer from "@/components/PageContainer.vue";
import {createPatient, createResult} from "@/services/api.js";

const name = ref('');
const marca = ref('');
const modelo = ref('');
const serial = ref('');
const responsable = ref('');
const foto = ref('');


const handleSubmit = async () => {
  // Validate form
  if (!name.value || !marca.value || !modelo.value ||
      !serial.value || responsable.value === '' || !foto.value ) {
    alert('Por favor, llene todos los campos');
    return;
  }

  const deviceData = {
    legalID: name.value,
    firstName: marca.value,
    lastName: modelo.value,
    age: serial.value,
    gender: responsable.value,
  };


//   try {
//     const {data: {patient: createdPatient}} = await createPatient(patientData);
//     await createResult({...lipidProfileData, patient: createdPatient._id});
//     resetForm();

//     alert('Patient and lipid profile created successfully');
//   } catch (error) {
//     console.error('Error creating patient or lipid profile:', error);
//     alert('Failed to create patient or lipid profile');
//   }
};
</script>

// Fetch professionals when the component is mounted
onMounted(fetchProfessionals);
</script>

<template>
  <PageContainer :showBanner="false">
    <div class="professionals">
      <div class="professionals-list">
        <h1>Lista de profesionales</h1>
        <div v-if="isLoading">Cargando profesionales...</div>
        <div v-else-if="error">{{ error }}</div>
        <table v-else>
          <thead>
          <tr>
            <th>Nombre</th>
            <th>Marca</th>
            <th>Modelo</th>
            <th>Serial</th>
            <th>Responsable</th>
            <th>Foto</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="device in devices" :key="device.document">
            <td>{{ device.nombre }}</td> <!-- Mostrar solo el Documento -->
            <td>{{ device.marca }}</td>
            <td>{{ device.modelo }}</td>
            <td>{{ device.serial }}</td>
            <td>{{ device.responsable }}</td>
            <td>
              <button class="action-btn view" @click="viewPatient(professional.id)">🔍</button>
              <button class="action-btn update" @click="handleUpdatePatient(professional.id)">🔄</button>
              <button class="action-btn delete" @click="handleDeletePatient(professional.id)">❌</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
      <div class="btn-container">
        <router-link to="/new-professional">
          <button class="btn btn-primary">Nuevo professional</button>
        </router-link>
        <router-link to="/">
          <button class="btn btn-secondary">Volver</button>
        </router-link>
      </div>
    </div>
  </PageContainer>
</template>

<style scoped>
.professionals {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 20px;
  width: 100%;
  min-height: 300px;
}

.professionals-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  width: 70%;


  table {
    width: 80%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }

  th, td {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
  }
}

.btn-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  gap: 20px;
}

.action-btn {
  background: none;
  border: none;
  cursor: pointer;
}

.action-btn.view:hover {
  color: blue;
}

.action-btn.update:hover {
  color: green;
}

.action-btn.delete:hover {
  color: red;
}

.btn {
  width: 200px;
  margin: 5px;
}
</style>
