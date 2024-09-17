let recorder;
let audioBlob;

const startRecording = async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        recorder = new MediaRecorder(stream);
        recorder.start();

        const audioChunks = [];
        recorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        recorder.onstop = () => {
            audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            document.getElementById("stopRecord").disabled = true;
            processAudio();
        };

        document.getElementById("startRecord").disabled = true;
        document.getElementById("stopRecord").disabled = false;
    } catch (error) {
        console.error("Erro ao iniciar gravação:", error);
    }
};

const stopRecording = () => {
    recorder.stop();
};

const processAudio = async () => {
    const formData = new FormData();
    formData.append("audio", audioBlob);

    try {
        const response = await fetch('https://us-central1-innate-path-421902.cloudfunctions.net/function-2', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const audioBlob = await response.blob();
            const audioUrl = URL.createObjectURL(audioBlob);

            const audioPlayer = document.getElementById('audioPlayback');

            audioPlayer.src = audioUrl;
            audioPlayer.play();
        } else {
            console.error("Erro no processamento de áudio:", response.statusText);
        }
    } catch (error) {
        console.error("Erro ao enviar o áudio:", error);
    }

    document.getElementById("startRecord").disabled = false;
};