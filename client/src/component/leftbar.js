import React from 'react';
import "leftbar.css"
export default function leftbar(){
  return(
    <div class="LeftbarMainContainer">
      <div class="website-logo">ADP<span class="dot">.</span></div>
      <div>
        <p class="menu-font">Menu</p>
        <ul>
            <li>
                <img src="" class="leftbar-icon" alt=""/>
                <p class ="leftbar-item">Browse</p>
            </li>
            <li>
                <img src="" class="leftbar-icon"  alt=""/>
                <p class ="leftbar-item">Watchlist</p>
            </li>
            <li>
                <img src="" class="leftbar-icon" alt=""/>
                <p class ="leftbar-item">Coming Soon</p>
            </li>
        </ul>
      </div>
    </div>
  )
}
