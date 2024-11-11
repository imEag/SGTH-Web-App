<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import PageContainer from '@/components/PageContainer.vue';
import { getAllProfessionals, deleteProfessional } from '@/services/api.js';

const router = useRouter();
const professionals = ref([]);
const isLoading = ref(true);
const error = ref(null);

// Fetch professionals from the database
const fetchProfessionals = async () => {
  try {
    isLoading.value = true;
    const response = await getAllProfessionals();
    console.log('response', response);
    professionals.value = response.data;
  } catch (err) {
    console.error('Error fetching professionals:', err);
    error.value = err.response?.data?.message || 'Failed to load professionals. Please try again.';
  } finally {
    isLoading.value = false;
  }
};

// Handle view professional action
const viewPatient = async (document) => {
  try {
    await router.push(`/professional/${document}`);
  } catch (err) {
    console.error('Error fetching professional details:', err);
    error.value = err.response?.data?.message || 'Failed to load professional details. Please try again.';
  }
};

// Handle update professionals action
const handleUpdatePatient = async (document) => {
  await router.push(`/professional/${document}`);
};

// Handle delete professionals action
const handleDeletePatient = async (id) => {
  if (confirm('Are you sure you want to delete this professionals?')) {
    try {
      await deleteProfessional(id);
      await fetchProfessionals(); // Refresh the list after deletion
    } catch (err) {
      console.error('Error deleting professionals:', err);
      error.value = err.response?.data?.message || 'Failed to delete professional. Please try again.';
    }
  }
};

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
            <th>ID</th>
            <th>Documento</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Correo</th>
            <th>Acciones</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="professional in professionals" :key="professional.document">
            <td>{{ professional.id }}</td> <!-- Mostrar solo el Documento -->
            <td>{{ professional.document }}</td>
            <td>{{ professional.first_name }}</td>
            <td>{{ professional.last_name }}</td>
            <td>{{ professional.email }}</td>
            <td>
              <button class="action-btn view" @click="viewPatient(professional.id)">🔍</button>
              <button class="action-btn delete" @click="handleDeletePatient(professional.id)">❌</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
      <div class="btn-container">
        <router-link to="/new-professional">
          <button class="btn btn-primary">Nuevo profesional</button>
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
