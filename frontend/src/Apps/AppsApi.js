import axios from 'axios';
const API_URL = 'http://localhost:8000';

const AppsApi = {

    getApps: function() {
        const url = `${API_URL}/api/apps/`;
        return axios.get(url).then(response => response.data);
    },
    getAppsByURL: function(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    },
    getApp: function(id) {
        const url = `${API_URL}/api/apps/${id}`;
        return axios.get(url).then(response => response.data);
    },
    deleteApp: function(app){
        const url = `${API_URL}/api/apps/${app.id}`;
        return axios.delete(url);
    },
    createApp: function(app){
        const url = `${API_URL}/api/apps/`;
        return axios.post(url,app);
    },
    updateApp: function(app){
        const url = `${API_URL}/api/apps/${app.id}`;
        return axios.put(url,app);
    },
}

export default AppsApi
