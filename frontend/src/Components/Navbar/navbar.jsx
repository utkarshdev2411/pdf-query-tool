import { IoIosAddCircleOutline } from "react-icons/io";
import logo from '../../assets/image.png';
import './navbar.css';

const Navbar = () => {
  const uploadFile = () => {
    const fileInput = document.getElementById('fileInput');
    fileInput.click();
  };

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const formData = new FormData();
      formData.append('file', file, 'sample.pdf');

      try {
        const response = await fetch('http://127.0.0.1:8000/pdf', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          console.log('File uploaded successfully');
        } else {
          console.error('File upload failed');
        }
      } catch (error) {
        console.error('Error uploading file:', error);
      }
    }
  };

  return (
    <div className='navbar'>
      <div className='logo'>
        <img src={logo} alt="Logo" />
      </div>
      <div className='upload'>
        <button onClick={uploadFile}>
          <IoIosAddCircleOutline size={20} /> Upload PDF
        </button>
        <input
          type="file"
          id="fileInput"
          style={{ display: 'none' }}
          onChange={handleFileChange}
        />
      </div>
    </div>
  );
};

export default Navbar;