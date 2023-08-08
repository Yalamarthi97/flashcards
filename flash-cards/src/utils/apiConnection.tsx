import axios from "axios";

export default axios.create({
    baseURL: "host.docker.internal:5555/v1"
})