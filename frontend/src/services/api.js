import axios from 'axios';

// const API_URL = 'http://localhost:5173/api'  // Ajusta según tu configuración

export const getAllProfessionals = () => {
  return axios.get('/professionals');
};

export const deleteProfessional = (id) => {
  return axios.delete(`/professionals/${id}`);
};
