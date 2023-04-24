import React from "react";
import LazyHero from "react-lazy-hero";

const HeroComponent = (props) => {
  return (
    <div>
      <LazyHero
        parallaxOffset={100}
        imageSrc={props.images}
        opacity={0.4}
        minHeight="20vh"
        style={{ maxWidth: "100%" }}
      >
        <h1>{props.headline}</h1>
        <h2>{props.description}</h2>
      </LazyHero>
    </div>
  );
};

export default HeroComponent;
