import React from "react";
import { PlayArrow } from "@material-ui/icons";
import { getMovieCastData, getMovieData, getRecommendedMoviesData } from "../API/utils.js";
import Youtube from "react-youtube";
// Images
import "./style/Movie.css";

const Movie = () => {
  return (
    <div className="featured">
      <img className="image" src="https://i.imgur.com/g5JNdYL.jpg" alt="" />
      <div className="data-content">
        <div className="left-content">
          <h1 className="title">Movie Name</h1>
          <div className="buttons">
            <button className="play">
              <PlayArrow /> <span>Play Now</span>
            </button>
            <button className="Trailer">
              <PlayArrow /> <span>Trailer</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Movie;
