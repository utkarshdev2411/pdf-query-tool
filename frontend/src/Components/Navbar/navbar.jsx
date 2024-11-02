import logo from '../../assets/image.png'
import { IoIosAddCircleOutline } from "react-icons/io";

import './navbar.css'

const Navbar = () => {
  const uploadFile = () => {
    const fileInput = document.getElementById('fileInput');
    fileInput.click();
  }

  return (
    <div className='navbar'>
      <div className='logo'>
        <img src={logo} alt="Logo" />
      </div>
      <div className='upload'>
        
        <button onClick={uploadFile}><IoIosAddCircleOutline size={20} />Upload PDF</button>
        <input type="file" id="fileInput" style={{ display: 'none' }} />
      </div>
    </div>
  )
}

export default Navbar