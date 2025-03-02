import './App.css';
import {useEffect, useState} from "react";
import axios from "axios";

function App() {
    const [messages, setMessages] = useState([
        {text: 'Hola! Bienvenido al chatbot de aprende leyendo.', isBot: true},
    ]);
    const [inputMessage, setInputMessage] = useState('');
    const [isLoading, setIsloading] = useState(false);
    const [isListening, setIsListening] = useState(false);

    const startVoiceRecognition = async () => {
        setIsListening(true);
        setIsloading(true);

        try {
            // Add visual feedback
            setMessages(prev => [...prev, {
                text: "Escuchando... Por favor, hable ahora.",
                isBot: true
            }]);
            const response = await axios.get('http://localhost:8000/voz', {
                timeout: 60000
            });

            if (response.data.status === 'success') {
                const {pregunta, respuesta} = response.data;
                if (pregunta) {
                    setMessages(prev => [...prev, {text: pregunta, isBot: false}]);
                    setMessages(prev => [...prev, {text: respuesta, isBot: true}]);
                }
            } else if (response.data.status === 'timeout') {
                setMessages(prev => [...prev, {
                    text: "Lo siento, no escuché nada. Por favor, inténtalo de nuevo.",
                    isBot: true
                }]);
            }
        } catch (e) {
            console.error('Error:', e);
            setMessages(prev => [...prev, {
                text: "Error al procesar el audio. Por favor, inténtalo de nuevo.",
                isBot: true
            }]);
        } finally {
            setIsloading(false);
            setIsListening(false);
        }
    }
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!inputMessage.trim()) return;

        // Add user message
        setMessages(prev => [...prev, {text: inputMessage, isBot: false}]);
        setIsloading(true);

        try {
            const response = await axios.post('http://localhost:8000/preguntar', {
                pregunta: inputMessage
            });
            // Add bot response
            setMessages(prev => [...prev, {text: response.data.respuesta, isBot: true}]);
        } catch (error) {
            console.error('Error:', error);
            setMessages(prev => [...prev, {
                text: "Lo siento, ahora mismo tenemos problemas técnicos para enviar tu mensaje. Por favor, inténtalo más tarde.",
                isBot: true
            }]);
        }
        setIsloading(false);
        setInputMessage('');
    };

    //HTML
    return (
        <div className="container mt-5 bg-opacity-10 bg-secondary">
            <div className="row justify-content-center">
                <div className="col-md-8">
                    <div className="card bg-secondary">
                        <div className="card-header bg-black text-white text-center">
                            <h2 className="mb-0">Chat</h2>
                        </div>
                        <div className="card-body chat-container" style={{height: '400px', overflowY: 'auto'}}>
                            {messages.map((message, index) => (
                                <div key={index}
                                     className={`d-flex ${message.isBot ? 'justify-content-start' : 'justify-content-end'} mb-3`}>
                                    <div
                                        className={`message p-2 rounded ${message.isBot ? 'bg-light' : 'bg-primary text-white'}`}
                                        style={{maxWidth: '70%'}}>
                                        {message.text}
                                    </div>
                                </div>
                            ))}
                            {isLoading && (
                                <div className="text-center">
                                    <div className="spinner-border text-primary" role="status">
                                        <span className="visually-hidden">Loading...</span>
                                    </div>
                                </div>
                            )}
                        </div>
                        <div className="card-footer">
                            <form onSubmit={handleSubmit}>
                                <div className="input-group">
                                    <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Escribe tu mensaje..."
                                        value={inputMessage}
                                        onChange={(e) => setInputMessage(e.target.value)}
                                    />
                                    <button className="btn btn-dark" type="submit">
                                        Enviar
                                    </button>
                                    <button
                                        className={`btn ${isListening ? 'btn-danger' : 'btn-success'}`}
                                        type={'button'}
                                        onClick={startVoiceRecognition}
                                        disabled={isListening}
                                    >
                                        <i className={`bi ${isListening ? 'bi-mic-fill' : 'bi-mic'}`}></i>
                                        {' '}
                                        {isListening ? 'Escuchando...' : 'Usar Voz'}
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default App;
