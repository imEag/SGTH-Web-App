import axios from 'axios';

// Definición de la URL base de la API
const API_URL = 'http://localhost:8000/api/';

// Función para obtener todos los profesionales
export const getAllProfessionals = async () => {
  try {
    const response = await axios.get(`${API_URL}professionals/`); // Usa API_URL para no repetir la URL
    return response; // Asegúrate de que la respuesta tenga una propiedad 'data' que contenga la lista de profesionales
  } catch (error) {
    console.error('Error al cargar los profesionales:', error);
    throw error;
  }
};

// Función para eliminar un profesional por su ID
export const deleteProfessional = (id) => {
  return axios.delete(`${API_URL}professionals/delete/${id}/`);
};

// Función para guardar un nuevo equipo
export const saveDevice = async (deviceData) => {
  try {
    const response = await axios.post(`${API_URL}devices-create/`, deviceData); // Corregí la URL eliminando la comilla extra
    return response.data;
  } catch (error) {
    console.error('Error al guardar el equipo:', error);
    throw error;
  }
};

export const getAllDevices = async () => {
  try {
    const response = await axios.get(`${API_URL}devices/`);
    console.log("Respuesta de la API:", response); // Para verificar toda la respuesta
    return response.data; // Retorna todos los equipos
  } catch (error) {
    console.error('Error al obtener los equipos:', error);
    throw error;
  }
};

// Función para eliminar un equipo por su ID
export const deleteDevice = (id) => {
  return axios.delete(`${API_URL}devices/delete/${id}/`); // Cambié la URL para ser más acorde con un dispositivo
};

