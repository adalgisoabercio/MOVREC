import React from "react";
import "./style/Navbar.css";
const Search = () => {
  return (
    <div className="left">
      <i className="nav-search2"></i>
      <div className="search-form" id="searchform">
        <form action="" method="post">
          <input
            type="text"
            name="search"
            placeholder="Search here"
            id="keyword"
          />
        </form>
      </div>
    </div>
  );
};
export default Search;
