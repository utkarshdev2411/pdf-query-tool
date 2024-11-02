import { useState } from 'react';
import { IoIosAddCircleOutline } from "react-icons/io";
import logo from '../../assets/image.png';
import './navbar.css';

const Navbar = () => {
  // State to store the name of the uploaded file
  const [fileName, setFileName] = useState('');

  // Function to trigger the file input click event
  const uploadFile = () => {
    const fileInput = document.getElementById('fileInput');
    fileInput.click();
  };

  // Function to handle file selection and upload
  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      // Set the file name to be displayed
      setFileName(file.name);

      // Create a FormData object to send the file
      const formData = new FormData();
      formData.append('file', file, 'sample.pdf');

      try {
        // Send the file to the server
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
      {/* Logo section */}
      <div className='logo'>
        <img src={logo} alt="Logo" />
      </div>

      {/* Upload section */}
      <div className='upload'>
        {/* Display the file name if a file is selected */}
        {fileName && <span className='file-name'>{fileName}</span>}
        
        {/* Upload button */}
        <button onClick={uploadFile}>
          <IoIosAddCircleOutline size={20} /> <span>Upload PDF</span>
        </button>
        
        {/* Hidden file input */}
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