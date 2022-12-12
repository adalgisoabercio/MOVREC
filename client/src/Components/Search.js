import React from 'react';
import './style/Navbar.css'
const Search = () => {
    return(
        <div>
            <i class="nav-search2"></i>
            <div class="search-form" id="searchform">
                <form action="" method="post">
                    <input type="text" name="search" placeholder="Search here" id="keyword"/>
                </form>
            </div>
        </div>
    )
}
export default Search;