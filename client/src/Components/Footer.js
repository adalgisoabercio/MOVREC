import React from "react";
import "./style/Footer.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/free-brands-svg-icons";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="item1">
          <span style={{ paddingRight: 5 }}>Copyright ©</span>
          <span style={{ paddingLeft: 5 }}>
            {new Date().getFullYear()} ADP. All Rights Reserved.
          </span>
        </div>
        <a href="https://github.com/adalgisoabercio/MOVREC" className="item2">
          <FontAwesomeIcon icon={faGithub} />
        </a>
      </div>
    </footer>
  );
};

export default Footer;
