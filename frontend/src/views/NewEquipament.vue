<script setup>
import { ref, onMounted } from 'vue';
import PageContainer from "@/components/PageContainer.vue";
import { getAllProfessionals, saveDevice } from "@/services/api.js";

const equipmentName = ref('');
const brand = ref('');
const model = ref('');
const serial = ref('');
const responsible = ref('');
const professionals = ref([]);
const photoFile = ref(null);
const photoPreview = ref(''); // Para mostrar la vista previa de la imagen

const loadProfessionals = async () => {
  try {
    const response = await getAllProfessionals();
    professionals.value = response.data;
  } catch (error) {
    alert('Error al cargar los profesionales');
  }
};

onMounted(loadProfessionals);

const resetForm = () => {
  equipmentName.value = '';
  brand.value = '';
  model.value = '';
  serial.value = '';
  responsible.value = '';
  photoFile.value = null;
  photoPreview.value = '';
};

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    photoFile.value = file;
    // Crear URL para vista previa
    photoPreview.value = URL.createObjectURL(file);
  }
};

const handleSubmit = async () => {
  if (!equipmentName.value || !brand.value || !model.value || !serial.value || !responsible.value) {
    alert('Por favor, llene todos los campos');
    return;
  }

  const formData = new FormData();
  formData.append('name', equipmentName.value);
  formData.append('brand', brand.value);
  formData.append('area', model.value);
  formData.append('serial', serial.value);
  formData.append('responsible', responsible.value);
  
  if (photoFile.value) {
    formData.append('image', photoFile.value);
  }

  try {
    await saveDevice(formData);
    alert('Equipo guardado con éxito');
    resetForm();
  } catch (error) {
    console.error('Error al guardar:', error);
    alert('Error al guardar el equipo');
  }
};
</script>
<template>
  <PageContainer>
    <div class="equipment-form">
      <div class="header">
        <div class="logo-container">
        </div>
      </div>

      <form class="form-control" @submit.prevent="handleSubmit">
        <h2>Datos del equipo</h2>
        
        <div class="form-grid">
          <input 
            placeholder="Nombre" 
            class="input" 
            v-model="equipmentName" 
          />
          <input 
            placeholder="Marca" 
            class="input" 
            v-model="brand" 
          />
          <input 
            placeholder="Modelo" 
            class="input" 
            v-model="model" 
          />
          <input 
            placeholder="Serial" 
            class="input" 
            v-model="serial" 
          />
        </div>

        <div class="form-row">
          <div class="select-container">
            <select v-model="responsible" class="input">
              <option value="" disabled selected>Seleccione un responsable</option>
              <option v-for="professional in professionals" :key="professional.id" :value="professional.id">
                {{ professional.document }}
              </option>
            </select>
          </div>

          <div class="photo-section">
            <div class="photo-container">
              <img v-if="photoPreview" :src="photoPreview" class="photo-preview" alt="Vista previa" />
              <div v-else class="photo-placeholder"></div>
            </div>
            <div class="photo-info">
              <p>Foto</p>
              <p>Adjuntar archivo</p>
              <input
                type="file"
                accept="image/*"
                @change="handleFileChange"
                ref="fileInput"
                style="display: none"
              />
              <button 
                type="button" 
                class="btn btn-upload"
                @click="$refs.fileInput.click()"
              >
                Adjuntar
              </button>
            </div>
          </div>
        </div>

        <div class="buttons-container">
          <router-link to="/devices-list">
            <button class="btn btn-secondary" type="button">Volver</button>
          </router-link>
          <button class="btn btn-primary" type="submit">Ingresar</button>
          <router-link to="/">
            <button class="btn btn-secondary" type="button" @click="resetForm">SALIR</button>
          </router-link>
        </div>
      </form>
    </div>
    <footer class="footer">
    </footer>
  </PageContainer>
</template>

<style lang="scss" scoped>
.photo-section {
    display: flex;
    gap: 1rem;

    .photo-container {
      width: 200px;
      height: 150px;
      border: 2px solid #ccc;
      border-radius: 10px;
      overflow: hidden;
      
      .photo-preview {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }

    .photo-placeholder {
      width: 100%;
      height: 100%;
      background: #f8f9fa;
    }

    .photo-info {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      text-align: left;
    }
  }

.equipment-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  min-height: 80vh;

  .header {
    text-align: center;
    margin-bottom: 2rem;

    h1 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
    }
  }

  .logo-container {
    position: relative;
    width: 100px;
    height: 60px;
    margin: 0 auto;

    .heartbeat-line {
      position: absolute;
      width: 100%;
      height: 2px;
      background: #00B4D8;
      top: 50%;
    }

    .plus-icon {
      position: absolute;
      width: 40px;
      height: 40px;
      background: #00B4D8;
      border-radius: 50%;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
    }
  }

  .form-control {
    width: 100%;
    max-width: 1200px;

    h2 {
      text-align: left;
      margin-bottom: 2rem;
    }
  }

  .form-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .input {
    width: 100%;
    padding: 0.8rem 1rem;
    border: 2px solid #ccc;
    border-radius: 25px;
    font-size: 1rem;
    outline: none;

    &:focus {
      border-color: #00B4D8;
    }
  }

  .select-container {
    position: relative;

    .select-arrow {
      position: absolute;
      right: 1rem;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
      font-size: 0.8rem;
    }

    select {
      appearance: none;
      width: 100%;
    }
  }

  .photo-section {
    display: flex;
    gap: 1rem;

    .photo-placeholder {
      width: 200px;
      height: 150px;
      border: 2px solid #ccc;
      border-radius: 10px;
      background: #f8f9fa;
    }

    .photo-info {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      text-align: left;
    }
  }

  .buttons-container {
    display: flex;
    justify-content: space-between;
    margin-top: 4rem;
    gap: 2rem;
  }

  .btn {
    padding: 0.8rem 2.5rem;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;

    &-primary {
      background: #00B4D8;
      color: white;

      &:hover {
        background: #0096c7;
      }
    }

    &-secondary {
      background: #E2E8F0;
      color: #1a202c;

      &:hover {
        background: #CBD5E0;
      }
    }

    &-upload {
      background: #E2E8F0;
      padding: 0.5rem 1.5rem;
      border-radius: 20px;

      &:hover {
        background: #CBD5E0;
      }
    }
  }
}

.footer {
  background: linear-gradient(to right, #2C7A7B, #00B4D8);
  color: white;
  padding: 1rem;
  text-align: center;
  width: 100%;

  h2 {
    margin: 0;
    font-size: 1.5rem;
  }
}
</style>
