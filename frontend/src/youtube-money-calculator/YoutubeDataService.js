import axios from 'axios';

class YoutubeDateService {
    calculate(channelUrl) {
        return axios.get(`http://127.0.0.1:5000/channels/${channelUrl}`);  // TODO
    }
}

export default new YoutubeDateService();
