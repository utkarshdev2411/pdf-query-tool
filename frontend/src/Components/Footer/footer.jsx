import "./footer.css";
import { LuSendHorizonal } from "react-icons/lu";


const ChatInput = () => {
  return (
    <div className="chat-input-container">
      <input
        type="text"
        className="chat-input"
        placeholder="Send a message..."
      />
      <button className="send-button"><LuSendHorizonal size={24} />
</button>
    </div>
  );
};

export default ChatInput;
