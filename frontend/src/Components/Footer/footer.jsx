import React from "react";
import "./footer.css";

const ChatInput = () => {
  return (
    <div className="chat-input-container">
      <input
        type="text"
        className="chat-input"
        placeholder="Send a message..."
      />
      <button className="send-button">➤</button>
    </div>
  );
};

export default ChatInput;
