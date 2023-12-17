import React from 'react'
import './Navbar.css'

function Navbar() {
    return (
        <nav className="navbar">
            <a href="#" className="navbar-brand logo">
            </a>
            <div className="navbar-items">
                <a href="#" className="navbar-item">Home</a>
                <a href="#" className="navbar-item">About</a>
            </div>
        </nav>
    );
}

export default Navbar;