import axios from 'axios';

export const getAllProfessionals = async () => {
    try {
        const response = await axios.get(`professionals/`);
        return response;
    } catch (error) {
        console.error('Error al cargar los profesionales:', error);
        throw error;
    }
};

export const deleteProfessional = (id) => {
    return axios.delete(`professionals/delete/${id}/`);
};

export const saveDevice = async (deviceData) => {
    try {
        const response = await axios.post(`devices/create/`, deviceData);
        return response.data;
    } catch (error) {
        console.error('Error al guardar el equipo:', error);
        throw error;
    }
};

export const getAllDevices = async () => {
    try {
        const response = await axios.get(`devices/`);
        console.log("Respuesta de la API:", response);
        return response.data;
    } catch (error) {
        console.error('Error al obtener los equipos:', error);
        throw error;
    }
};

export const deleteDevice = (id) => {
    return axios.delete(`devices/delete/${id}/`);
};

export const saveProfessional = async (professionalData) => {
    try {
        const response = await axios.post(`professionals/create/`, professionalData);
        return response.data;
    } catch (error) {
        console.error('Error al guardar el profesional:', error);
        throw error;
    }
}

export const getProfessional = async (id) => {
    try {
        const response = await axios.get(`professionals/${id}/`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener el profesional:', error);
        throw error;
    }
}

export const updateProfessional = async (id, professionalData) => {
    try {
        const response = await axios.put(`professionals/update/${id}/`, professionalData);
        return response.data;
    } catch (error) {
        console.error('Error al actualizar el profesional:', error);
        throw error;
    }
}


export const updateDevice = async (id, deviceData) => {
  try {
      const response = await axios.put(`devices/update/${id}/`, deviceData);
      return response.data;
  } catch (error) {
      console.error('Error al actualizar el equipo:', error);
      throw error;
  }
};

export const getDevice = async (id) => {
  try {
      const response = await axios.get(`devices/${id}/`);
      return response.data;
  } catch (error) {
      console.error('Error al obtener el equipo:', error);
      throw error;
  }
};
