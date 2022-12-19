import React from "react";
import HeroSlider, { Slide, Nav } from "hero-slider";
import { InfoOutlined } from "@material-ui/icons";
// Images
import "./style/Recommendation.css";

const Recommendation = () => {
  return (
    <HeroSlider
      height={"100vh"}
      autoplay
      controller={{
        initialSlide: 1,
        slidingDuration: 500,
        slidingDelay: 100,
        onSliding: (nextSlide) =>
          console.debug("onSliding(nextSlide): ", nextSlide),
        onBeforeSliding: (previousSlide, nextSlide) =>
          console.debug(
            "onBeforeSliding(previousSlide, nextSlide): ",
            previousSlide,
            nextSlide
          ),
        onAfterSliding: (nextSlide) =>
          console.debug("onAfterSliding(nextSlide): ", nextSlide)
      }}
    >
      <Slide
        shouldRenderMask
        navDescription="ADP 2022"
        background={{
          backgroundImageSrc: "https://i.imgur.com/g5JNdYL.jpg"
        }}
      >
        <div className="heroContent">
          <div className="leftContent">
            <h1 className="title">Movie Name</h1>
            <div className="buttons">
              <button className="play">
                <InfoOutlined /> <span>More Info</span>
              </button>
            </div>
          </div>
        </div>
      </Slide>
      <Slide
        shouldRenderMask
        navDescription="ADP 2022"
        background={{
          backgroundImageSrc: "https://i.imgur.com/XpreppQ.jpeg"
        }}
      >
        <div className="heroContent">
          <div className="leftContent">
            <h1 className="title">Keanu Reaves</h1>
            <div className="buttons">
              <button className="play">
                <InfoOutlined /> <span>More Info</span>
              </button>
            </div>
          </div>
        </div>
      </Slide>
      <Slide
        shouldRenderMask
        navDescription="ADP 2022"
        background={{
          backgroundImageSrc: "https://i.imgur.com/VJhOuhK.jpeg"
        }}
      >
        <div className="heroContent">
          <div className="leftContent">
            <h1 className="title">Star Wars</h1>
            <div className="buttons">
              <button className="play">
                <InfoOutlined /> <span>More Info</span>
              </button>
            </div>
          </div>
        </div>
      </Slide>
      <Nav />
    </HeroSlider>
  );
};

export default Recommendation;
