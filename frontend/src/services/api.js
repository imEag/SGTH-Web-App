import axios from 'axios';

export const getAllProfessionals = () => {
  return axios.get('/professionals');
};

export const deleteProfessional = (id) => {
  return axios.delete(`/professionals/${id}`);
};