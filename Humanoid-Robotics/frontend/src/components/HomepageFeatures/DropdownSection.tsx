import React, { useState } from 'react';

export default function DropdownSection({ title, children }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="dropdown-section">
      <button onClick={() => setOpen(!open)} className="dropdown-header">
        {title}
        <span>{open ? '−' : '+'}</span>
      </button>

      {open && <div className="dropdown-content">{children}</div>}
    </div>
  );
}
