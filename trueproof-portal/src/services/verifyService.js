export async function verifyFile(formData) {
  const response = await fetch("http://localhost:8000/api/verify", {
    method: "POST",
    body: formData,
  });
  return await response.json();
}