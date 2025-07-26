import React, { useState } from 'react';
import FileUpload from '../components/FileUpload';
import { verifyFile } from '../services/verifyService';

export default function UploadPage() {
  const [result, setResult] = useState(null);

  const handleUpload = async (formData) => {
    const res = await verifyFile(formData);
    setResult(res);
  };

  return (
    <div className="max-w-xl mx-auto mt-10">
      <h1 className="text-2xl font-bold mb-4">Verify Media</h1>
      <FileUpload onUpload={handleUpload} />
      {result && (
        <div className="mt-6 p-4 bg-gray-100 rounded shadow">
          <h2 className="text-xl font-semibold">Result</h2>
          <p><strong>Verdict:</strong> {result.verdict}</p>
          <p><strong>Score:</strong> {result.manipulation_score}</p>
          <p><strong>Model:</strong> {result.model}</p>
        </div>
      )}
    </div>
  );
}