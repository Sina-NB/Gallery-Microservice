import React, {useEffect, useState} from 'react';
import Wrapper from "./Wrapper";
import {Photo} from "../interfaces/photo";
import {Link} from "react-router-dom";

const Photos = () => {
    const [photos, setPhotos] = useState([]);

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://localhost:8000/api/photos');

                const data = await response.json();

                setPhotos(data);
            }
        )();
    }, []);

    const del = async (id: number) => {
        if (window.confirm('Are you sure you want to delete this photo?')) {
            await fetch(`http://localhost:8000/api/photos/${id}`, {
                method: 'DELETE'
            });

            setPhotos(photos.filter((p: Photo) => p.id !== id));
        }
    }

    return (
        <Wrapper>
            <div className="pt-3 pb-2 mb-3 border-bottom">
                <div className="btn-toolbar mb-2 mb-md-0">
                    <Link to='/admin/photos/create' className="btn btn-sm btn-outline-secondary">Add</Link>
                </div>
            </div>

            <div className="table-responsive">
                <table className="table table-striped table-sm">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Image</th>
                        <th>Title</th>
                        <th>Likes</th>
                        <th>Action</th>
                    </tr>
                    </thead>
                    <tbody>
                    {photos.map(
                        (p: Photo) => {
                            return (
                                <tr key={p.id}>
                                    <td>{p.id}</td>
                                    <td><img src={p.image} height="180"/></td>
                                    <td>{p.title}</td>
                                    <td>{p.likes}</td>
                                    <td>
                                        <div className="btn-group mr-2">
                                            <Link to={`/admin/photos/${p.id}/edit`}
                                                  className="btn btn-sm btn-outline-secondary">Edit</Link>
                                            <a href="#" className="btn btn-sm btn-outline-secondary"
                                               onClick={() => del(p.id)}
                                            >Delete</a>
                                        </div>
                                    </td>
                                </tr>
                            )
                        })}

                    </tbody>
                </table>
            </div>
        </Wrapper>
    );
};

export default Photos;
