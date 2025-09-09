import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";   // 👈 VERY IMPORTANT (brings in Tailwind + your custom styles)

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
