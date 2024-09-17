let mediaRecorder;
let audioChunks = [];

const recordButton = document.getElementById("record-button");

const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    recordButton.textContent = "Gravando... Clique para parar.";
    recordButton.removeEventListener('click', startRecording);
    recordButton.addEventListener('click', stopRecording);

    mediaRecorder.addEventListener("dataavailable", event => {
        audioChunks.push(event.data);
    });
};

const stopRecording = async () => {
    mediaRecorder.stop();

    recordButton.textContent = "Gravar Áudio";
    recordButton.removeEventListener('click', stopRecording);
    recordButton.addEventListener('click', startRecording);

    mediaRecorder.addEventListener("stop", async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        audioChunks = [];
        const formData = new FormData();
        formData.append('audio', audioBlob);

        try {
            const response = await fetch('/transcribe-and-dialogflow', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();

            document.getElementById("transcription").innerText = data.transcription;
            document.getElementById("response").innerText = data.dialogflowResponse;
        } catch (error) {
            console.error('Erro ao transcrever ou enviar ao Dialogflow:', error);
        }
    });
};

// Inicializar o botão de gravação
recordButton.addEventListener('click', startRecording);