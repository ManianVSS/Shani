import React from "react";
import LazyHero from "react-lazy-hero";

const HeroComponent = (props) => {
  return (
    <div>
      <LazyHero parallaxOffset={100} imageSrc={props.images} opacity={0.4}>
        <h1>{props.headline}</h1>
      </LazyHero>
    </div>
  );
};

export default HeroComponent;
