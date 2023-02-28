import React, { useEffect } from "react";
import { useRecoilState } from "recoil";
import { authState } from "../../state/authData";

const Home = () => {
  const [userData, setUserData] = useRecoilState(authState);
  useEffect(() => {
    setUserData({
      accessToken: window.localStorage.getItem("accessToken"),
      authStatus: true,
      errorMessage: "",
      userName: window.localStorage.getItem("user"),
    });
  }, []);
  return <div>Home</div>;
};

export default Home;
