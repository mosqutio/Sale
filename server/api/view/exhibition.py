

def exhibition_to_dict(exhibitions):
    if isinstance(exhibitions, list):
        view = []
        for exhibition in exhibitions:
            view.append(exhibition_to_dict(exhibition))
        return view
    else:
        view = dict()
        view['created_at'] = exhibitions.created_at
        view['updated_at'] = exhibitions.updated_at
        view['deleted_at'] = exhibitions.deleted_at
        view['id'] = exhibitions.id
        view['locale'] = exhibitions.locale
        view['owner'] = exhibitions.owner
        view['end_time'] = exhibitions.end_time
        view['start_time'] = exhibitions.start_time
        view['description'] = exhibitions.description
    return view


if __name__ == "__main__":
    from server.db import db
    e = db.Exhibition()
    a = exhibition_to_dict([e])
    print(a)
