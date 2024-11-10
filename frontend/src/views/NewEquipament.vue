<script setup>
import { ref } from 'vue';
import PageContainer from "@/components/PageContainer.vue";

const equipmentName = ref('');
const brand = ref('');
const model = ref('');
const serial = ref('');
const responsible = ref('');

const resetForm = () => {
  equipmentName.value = '';
  brand.value = '';
  model.value = '';
  serial.value = '';
  responsible.value = '';
};

const handleSubmit = async () => {
  if (!equipmentName.value || !brand.value || !model.value || !serial.value || !responsible.value) {
    alert('Por favor, llene todos los campos');
    return;
  }
};
</script>

<template>
  <PageContainer>
    <div class="equipment-form">
      <div class="header">
        <h1>SGTH</h1>
        <div class="logo-container">
          <div class="heartbeat-line"></div>
          <div class="plus-icon">+</div>
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
              <option value="" disabled selected>Responsable</option>
              <option value="1">Responsable 1</option>
              <option value="2">Responsable 2</option>
            </select>
            <span class="select-arrow">▼</span>
          </div>

          <div class="photo-section">
            <div class="photo-placeholder"></div>
            <div class="photo-info">
              <p>Foto</p>
              <p>Adjuntar archivo</p>
              <button type="button" class="btn btn-upload">Adjuntar</button>
            </div>
          </div>
        </div>

        <div class="buttons-container">
          <router-link to="/equipments">
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
      <h2>Alma mater</h2>
    </footer>
  </PageContainer>
</template>

<style lang="scss" scoped>
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