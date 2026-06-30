'use client';
export default function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-xl shadow-2xl max-w-2xl w-full">
        <h1 className="text-3xl font-bold text-center text-blue-700 mb-4">
          🦷 Tutor Inteligente de Odontología
        </h1>
        <p className="text-center text-gray-600 mb-6">
          Dr. Mendoza te guiará en el aprendizaje adaptativo.
        </p>
        <div className="bg-blue-50 p-4 rounded-lg">
          <p className="text-sm text-gray-700">
            Sistema desplegado en Railway. ¡Funciona!
          </p>
        </div>
      </div>
    </div>
  );
}
