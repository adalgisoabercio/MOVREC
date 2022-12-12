import React from 'react';
import './style/Navbar.css'
import Search from './Search.js';
const Navbar = () => {
    var navbar = document.querySelector ('#navbar');
    document.addEventListener('scroll', () => { 
        var scroll_position = window.scrollY;
        if (scroll_position > 250) {
            navbar.style.backgroundColor = '#29323c';
        } else {
            navbar.style.backgroundColor = 'linear-gradient(to top, transparent 0%, rgb(0, 0, 0, 0.3) 50%)' ;
        }
    });    
    return(
        
        <div id ="navbar" className="navbar">
            <div className="container">
                <div className="left">
                    <div className="logo-navbar">ADP<span>.</span>
                    </div>
                    <div className="navbar-link">
                        <span className="item-navbar">Movies</span>
                        <span className="item-navbar">My List</span>
                    </div>
                    <Search/>
                </div>
                <div className="right">
                    Login
                    <div className="profile">
                        <div className="options">
                        <span>Settings</span>
                        <span>Logout</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Navbar;
