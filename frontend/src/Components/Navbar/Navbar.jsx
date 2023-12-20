import React from 'react'
import { Link } from 'react-router-dom'
import './Navbar.css'

function Navbar() {
    return (
        <nav className="navbar">
            <Link to="/" className="navbar-brand logo">
            </Link>
            <div className="navbar-items">
            <Link to="/" className="navbar-item">Home</Link>
            <Link to="/about" className="navbar-item">About</Link>
            </div>
        </nav>
    );
}

export default Navbar;