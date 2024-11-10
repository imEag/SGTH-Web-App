<script setup>
import PageContainer from "@/components/PageContainer.vue";
import { ref, onMounted } from 'vue';
import { getAllDevices, deleteDevice } from "@/services/api.js";

const equipments = ref([]);
const loading = ref(true);
const error = ref(null);

// Función para obtener los dispositivos
const fetchDevices = async () => {
  try {
    loading.value = true;
    const response = await getAllDevices();
    equipments.value = Array.isArray(response.data) ? response.data : response;
  } catch (err) {
    console.error('Error al obtener los equipos:', err);
    error.value = 'Error al cargar los equipos. Por favor, intente nuevamente.';
  } finally {
    loading.value = false;
  }
};

// Función para eliminar un equipo
const removeDevice = async (id) => {
  try {
    await deleteDevice(id); // Llama a la función deleteDevice
    // Actualiza la lista de equipos después de eliminar el dispositivo
    equipments.value = equipments.value.filter(device => device.id !== id);
  } catch (err) {
    console.error('Error al eliminar el equipo:', err);
    error.value = 'Error al eliminar el equipo. Por favor, intente nuevamente.';
  }
};

onMounted(() => {
  fetchDevices();
});
</script>



<template>
  <PageContainer>
    <div class="inventory">
      <div class="top-buttons">
        <router-link to="/devices-create" class="btn btn-primary">Nuevo equipo</router-link>
        <router-link to="/" class="btn btn-secondary">Volver</router-link>
      </div>

      <header class="inventory__header">
        <h1>Alma mater</h1>
      </header>

      <div class="equipment-grid">
        <div v-for="equipment in equipments" 
             :key="equipment.id" 
             class="equipment-card">
          <div class="card-header"></div>
          <div class="card-stripe"></div>
          <div class="equipment-info">
            <img :src="equipment.image || '/default-image.jpg'" 
                 :alt="equipment.name" 
                 class="equipment-image">
            <div class="equipment-details">
              <h3 class="equipment-title">{{ equipment.name }}</h3>
              <p class="equipment-id">ID: {{ equipment.id }}</p>
              <p class="equipment-id">Serial: {{ equipment.serial || 'N/A' }}</p>
            </div>
          </div>
          <div class="equipment-area">
            <span class="area-text">Área: {{ equipment.area || 'Desconocida' }}</span>
            <div class="action-buttons">
              <button class="action-button" @click="removeDevice(equipment.id)">❌</button>
              <button class="action-button">⚙️</button>
            </div>
          </div>
        </div>
      </div>

      <div v-if="error" class="error-message">{{ error }}</div>

      <div class="pagination-buttons">
        <button class="btn btn-secondary">Anterior</button>
        <button class="btn btn-primary">Siguiente</button>
      </div>

      <div class="page-counter">
        <span>Página 1 de 10</span>
      </div>
    </div>
  </PageContainer>
</template>



<style lang="scss" scoped>
:root {
  --primary-color: #2A9D8F;
  --secondary-color: #E9ECEF;
  --accent-color: #007acc;
  --text-color: #333333;
  --header-color: #a0e4f1;
  --stripe-color: #e3f2fd;
  --border-color: rgba(0, 0, 0, 0.08);
  --focus-color: #ff8c00;
}

.inventory {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;

  &__header {
    background-color: var(--primary-color);
    color: white;
    padding: 15px;
    text-align: center;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

    h1 {
      margin: 0;
      font-family: Arial, sans-serif;
      font-size: 24px;
    }
  }
}

.top-buttons,
.pagination-buttons {
  display: flex;
  justify-content: center;
  gap: 12px; /* Ajustado el espacio entre los botones */
  margin: 10px 0;

  .btn {
    padding: 8px 16px; /* Botones más pequeños */
    font-size: 14px;
    border-radius: 6px;
    cursor: pointer;
    font-family: Arial, sans-serif;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;

    display: flex;
    justify-content: center;
    align-items: center;

    &:hover,
    &:focus {
      transform: translateY(-2px);
      box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    &:focus {
      outline: none;
      border: 2px solid var(--focus-color);
    }

    &-primary {
      background-color: #00aaff;
      color: white;
      box-shadow: 0 4px 6px rgba(0, 170, 255, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.1);

      &:hover {
        background-color: #0099cc;
      }
    }
    
    &-secondary {
      background-color: #a0e4f1;
      color: var(--text-color);
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border: 1px solid var(--border-color);

      &:hover {
        background-color: #85c0d2;
      }
    }
  }
}

.equipment-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;

  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(3, 1fr);
  }
}

.equipment-card {
  background: linear-gradient(135deg, #ffffff, #f7f9fc);
  border-radius: 12px;
  border: 2px solid rgba(42, 157, 143, 0.3);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1), 0 4px 8px rgba(0, 0, 0, 0.06);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 20px rgba(0, 0, 0, 0.12), 0 6px 10px rgba(0, 0, 0, 0.08);
    border-color: rgba(42, 157, 143, 0.5);
  }

  .card-header {
    background-color: var(--header-color);
    height: 8px;
    width: 100%;
  }

  .card-stripe {
    background-color: var(--stripe-color);
    height: 6px;
    width: 100%;
  }

  .equipment-info {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 20px;
  }

  .equipment-image {
    width: 90px;
    height: 90px;
    object-fit: contain;
    background-color: #f8f9fa;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    border: 1px solid var(--border-color);
  }

  .equipment-details {
    flex-grow: 1;
    text-align: left;
  }

  .equipment-title {
    font-size: 18px;
    margin: 0 0 8px 0;
    color: var(--text-color);
    font-family: Arial, sans-serif;
    font-weight: 600;
  }

  .equipment-id {
    font-size: 14px;
    color: #666;
    margin: 4px 0;
  }

  .equipment-area {
    background-color: var(--secondary-color);
    padding: 10px 15px;
    border-radius: 25px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 0 20px 20px 20px;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    border: 1px solid var(--border-color);
  }

  .area-text {
    font-size: 14px;
    color: var(--text-color);
    font-weight: 600;
  }

  .action-buttons {
    display: flex;
    gap: 8px;
  }

  .action-button {
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
    color: var(--accent-color);
    padding: 4px;
    transition: transform 0.2s ease;

    &:hover {
      transform: scale(1.1);
      opacity: 0.8;
    }
  }
}

/* Contador de página */
.page-counter {
  text-align: center;
  margin-top: 20px;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-color);
}
</style>