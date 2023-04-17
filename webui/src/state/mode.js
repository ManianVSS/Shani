import { atom } from "recoil";

export const colorScheme = atom({
  key: "colorScheme",
  default: "light",
});

export const sideBar = atom({
  key: "sideBar",
  default: "open",
});
