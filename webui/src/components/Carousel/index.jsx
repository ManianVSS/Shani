import React from "react";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from "react-responsive-carousel";
import TimerComponent from "../TimerComponent";

const ResponsiveCarousel = (props) => {
  return (
    <div>
      <Carousel
        autoPlay={props.autoPlay}
        showArrows={props.showArrows}
        showStatus={props.showStatus}
        showIndicators={props.showIndicators}
        showThumbs={props.showThumbs}
        transitionTime={props.transitionTime}
        infiniteLoop={props.infiniteLoop}
      >
        {props.componentListData.map((item) => {
          return <TimerComponent name={item.name} time={item.time} />;
        })}
      </Carousel>
    </div>
  );
};

export default ResponsiveCarousel;
