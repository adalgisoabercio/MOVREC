import React from 'react';
import Navbar from '../Components/Navbar';
import Recommendation from '../Components/Recommendation';
import MovieRecommendation from '../Components/MovieItem';
import './Style/Home.css';

const Home = () => {
    return(
        <div class="Home-Container">
            <Navbar />
            {/* <Recommendation /> */}
            <Recommendation />
            <MovieRecommendation />
        </div>
    );

}
export default Home;
