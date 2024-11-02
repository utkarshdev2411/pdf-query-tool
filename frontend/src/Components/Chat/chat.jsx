import { useState } from 'react';
import { LuSendHorizonal } from "react-icons/lu";
import './chat.css';
import UserLogo from '../../assets/user-logo.png';
import AiLogo from '../../assets/ai-logo.png';

const Chat = () => {
  // State to store chat messages
  const [messages, setMessages] = useState([]);
  // State to store the current input value
  const [input, setInput] = useState('');

  // Function to handle sending a message
  const sendMessage = async () => {
    // Prevent sending empty messages
    if (input.trim() === '') return;

    // Add the user's message to the chat
    const userMessage = { sender: 'user', text: input };
    setMessages([...messages, userMessage]);
    setInput('');

    try {
      // Send the user's message to the server
      const response = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_question: input }),
      });

      // Handle the server's response
      if (response.ok) {
        const data = await response.json();
        const aiMessage = { sender: 'ai', text: data.answer };
        setMessages((prevMessages) => [...prevMessages, aiMessage]);
      } else {
        console.error('Error fetching AI response');
      }
    } catch (error) {
      console.error('Error fetching AI response:', error);
    }
  };

  return (
    <div className="chat-container">
      {/* Display chat messages */}
      <div className="chat-messages">
        {messages.map((message, index) => (
          <div key={index} className={`chat-message ${message.sender}`}>
            <img
              src={message.sender === 'user' ? UserLogo : AiLogo}
              alt={`${message.sender} profile`}
              className="profile-image"
            />
            <div className="message-text">{message.text}</div>
          </div>
        ))}
      </div>
      {/* Input field and send button */}
      <div className="chat-input-container">
        <input
          type="text"
          className="chat-input"
          placeholder="Send a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button className="send-button" onClick={sendMessage}>
          <LuSendHorizonal size={24} />
        </button>
      </div>
    </div>
  );
};

export default Chat;