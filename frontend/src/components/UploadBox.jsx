import { UploadCloud } from 'lucide-react';

export default function UploadBox({ file, preview, onChange }) {
  return (
    <label className="upload-box glass-card">
      <input type="file" accept="image/png,image/jpeg,image/webp" onChange={onChange} />
      {preview ? (
        <img src={preview} alt="Selected sports equipment preview" className="preview-image" />
      ) : (
        <div className="upload-placeholder">
          <UploadCloud size={48} />
          <h3>Upload equipment image</h3>
          <p>JPG, PNG, or WEBP</p>
        </div>
      )}
      {file && <span className="file-name">{file.name}</span>}
    </label>
  );
}
