import React, { useState } from 'react';

const UploadImage = () => {
  const [selectedImage, setSelectedImage] = useState();
  const imageChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      setSelectedImage(e.target.files[0]);
    }
  };

  return (
    <div style={styles.container}>
      <input accept="image/*" type="file" onChange={imageChange} />

      {selectedImage && (
        <div style={styles.preview}>
          <img
            src={URL.createObjectURL(selectedImage)}
            width="100%"
            height="300"
            alt="Thumb"
          />
        </div>
      )}
    </div>
  );
};

export default UploadImage;

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    paddingTop: 50,
  },

  preview: {
    marginTop: 20,
    display: 'flex',
    flexDirection: 'column',
  },
};
