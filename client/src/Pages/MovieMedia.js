import React from "react";
import Navbar from "../Components/Navbar";
import Movie from "../Components/Movie";
import Footer from "../Components/Footer";
import MovieRecommendation from "../Components/MovieItem";
import "./Style/Home.css";

const MovieMedia = () => {
  return (
    <div class="Home-Container">
      <Navbar />
      <Movie />
      <MovieRecommendation />
      <Footer />
    </div>
  );
};
export default MovieMedia;
