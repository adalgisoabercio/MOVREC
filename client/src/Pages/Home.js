import React from 'react';
import Navbar from '../Components/Navbar';
import Recommendation from '../Components/Recommendation';
import './Style/Home.css';

const Home = () => {
    return(
        <div class="Home-Container">
            <Navbar />
            <Recommendation />
        </div>
    );

}
export default Home;
