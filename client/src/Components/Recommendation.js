import "./style/Recommendation.css";
import IMG from "./style/IMG.jpg";
export default function Recommendation() {
  return (
    <div className="featured">
      <img className="image"
        src={IMG}
      />
      <div className ="data-content">
        <div className="left-content">
          <div>NAMA FILM</div>

        </div>
        <div className="right-content">
          <img
                src={IMG} 
                alt=""
              />
        </div>
      </div>
    </div>
  );
}
