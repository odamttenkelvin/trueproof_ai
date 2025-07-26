import React, { useState } from 'react';

export default function FileUpload({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!file) return alert("Choose a file first!");

    const formData = new FormData();
    formData.append("file", file);
    onUpload(formData);
  };

  return (
    <div className="p-4 border rounded-xl shadow bg-white">
      <input type="file" onChange={handleChange} />
      <button onClick={handleUpload} className="mt-2 px-4 py-2 bg-blue-600 text-white rounded">
        Upload & Verify
      </button>
    </div>
  );
}