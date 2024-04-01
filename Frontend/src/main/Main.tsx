import React, {useEffect, useState} from 'react';
import {Photo} from "../interfaces/photo";

const Main = () => {
    const [photos, setPhotos] = useState([] as Photo[]);

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://localhost:8001/api/photos');

                const data = await response.json();

                setPhotos(data);
            }
        )();
    }, []);

    const like = async (id: number) => {
        await fetch(`http://localhost:8001/api/photos/${id}/like`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });

        setPhotos(photos.map(
            (p: Photo) => {
                if (p.id === id) {
                    p.likes++;
                }

                return p;
            }
        ));
    }

    return (
        <main role="main">
            <div className="album py-5 bg-light">
                <div className="container">
                    <div className="row">
                        {photos.map(
                            (p: Photo) => {
                                return (
                                    <div className="col-md-4" key={p.id}>
                                        <div className="card mb-4 shadow-sm">
                                            <img src={p.image} height="180"/>
                                            <div className="card-body">
                                                <p className="card-text">{p.title}</p>
                                                <div className="d-flex justify-content-between align-items-center">
                                                    <div className="btn-group">
                                                        <button type="button"
                                                                className="btn btn-sm btn-outline-secondary"
                                                                onClick={() => like(p.id)}
                                                        >
                                                            Like
                                                        </button>
                                                    </div>
                                                    <small className="text-muted">{p.likes} likes</small>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                )
                            }
                        )}
                    </div>
                </div>
            </div>

        </main>
    );
};

export default Main;
