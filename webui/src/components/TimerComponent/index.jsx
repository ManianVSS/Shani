import React, { useEffect, useState } from "react";
import "./style.css";
import { useRecoilValue } from "recoil";
import { timerState } from "../../state/timerData";

const TimerComponent = (props) => {
  // const timerData = useRecoilValue(timerState);
  return (
    <div>
      <div className="app">
        <div className="timer-container">
          <h1 className="header">{props.name}</h1>
          <Timer time={props.time} />
        </div>
      </div>
    </div>
  );
};

const Timer = (props) => {
  const [days, setDays] = React.useState(0);
  const [hours, setHours] = React.useState(0);
  const [minutes, setMinutes] = React.useState(0);
  const [seconds, setSeconds] = React.useState(0);
  // const timerData = useRecoilValue(timerState);

  const deadline = props.time;
  const getTime = () => {
    const time = Date.parse(deadline) - Date.now();

    setDays(Math.floor(time / (1000 * 60 * 60 * 24)));
    setHours(Math.floor((time / (1000 * 60 * 60)) % 24));
    setMinutes(Math.floor((time / 1000 / 60) % 60));
    setSeconds(Math.floor((time / 1000) % 60));
  };

  React.useEffect(() => {
    const interval = setInterval(() => getTime(deadline), 1000);
    return () => clearInterval(interval);
  }, [deadline]);

  return (
    <div className="timer" role="timer">
      <div className="timer-col-4">
        <div className="timer-box">
          <p id="day">{days < 10 ? "0" + days : days}</p>
          <span className="timer-text">Days</span>
        </div>
      </div>
      <div className="timer-col-4">
        <div className="timer-box">
          <p id="hour">{hours < 10 ? "0" + hours : hours}</p>
          <span className="timer-text">Hours</span>
        </div>
      </div>
      <div className="timer-col-4">
        <div className="timer-box">
          <p id="minute">{minutes < 10 ? "0" + minutes : minutes}</p>
          <span className="timer-text">Minutes</span>
        </div>
      </div>
      <div className="timer-col-4">
        <div className="timer-box">
          <p id="second">{seconds < 10 ? "0" + seconds : seconds}</p>
          <span className="timer-text">Seconds</span>
        </div>
      </div>
    </div>
  );
};
export default TimerComponent;
