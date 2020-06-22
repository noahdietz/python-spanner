# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/spanner_v1/proto/mutation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.cloud.spanner_v1.proto import (
    keys_pb2 as google_dot_cloud_dot_spanner__v1_dot_proto_dot_keys__pb2,
)
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/spanner_v1/proto/mutation.proto",
    package="google.spanner.v1",
    syntax="proto3",
    serialized_options=b"\n\025com.google.spanner.v1B\rMutationProtoP\001Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\252\002\027Google.Cloud.Spanner.V1\312\002\027Google\\Cloud\\Spanner\\V1",
    serialized_pb=b'\n,google/cloud/spanner_v1/proto/mutation.proto\x12\x11google.spanner.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a(google/cloud/spanner_v1/proto/keys.proto\x1a\x1cgoogle/api/annotations.proto"\xc6\x03\n\x08Mutation\x12\x33\n\x06insert\x18\x01 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00\x12\x33\n\x06update\x18\x02 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00\x12=\n\x10insert_or_update\x18\x03 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00\x12\x34\n\x07replace\x18\x04 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00\x12\x34\n\x06\x64\x65lete\x18\x05 \x01(\x0b\x32".google.spanner.v1.Mutation.DeleteH\x00\x1aS\n\x05Write\x12\r\n\x05table\x18\x01 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x02 \x03(\t\x12*\n\x06values\x18\x03 \x03(\x0b\x32\x1a.google.protobuf.ListValue\x1a\x43\n\x06\x44\x65lete\x12\r\n\x05table\x18\x01 \x01(\t\x12*\n\x07key_set\x18\x02 \x01(\x0b\x32\x19.google.spanner.v1.KeySetB\x0b\n\toperationB\x96\x01\n\x15\x63om.google.spanner.v1B\rMutationProtoP\x01Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1b\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        google_dot_cloud_dot_spanner__v1_dot_proto_dot_keys__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_MUTATION_WRITE = _descriptor.Descriptor(
    name="Write",
    full_name="google.spanner.v1.Mutation.Write",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="table",
            full_name="google.spanner.v1.Mutation.Write.table",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="columns",
            full_name="google.spanner.v1.Mutation.Write.columns",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="values",
            full_name="google.spanner.v1.Mutation.Write.values",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=459,
    serialized_end=542,
)

_MUTATION_DELETE = _descriptor.Descriptor(
    name="Delete",
    full_name="google.spanner.v1.Mutation.Delete",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="table",
            full_name="google.spanner.v1.Mutation.Delete.table",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="key_set",
            full_name="google.spanner.v1.Mutation.Delete.key_set",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=544,
    serialized_end=611,
)

_MUTATION = _descriptor.Descriptor(
    name="Mutation",
    full_name="google.spanner.v1.Mutation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="insert",
            full_name="google.spanner.v1.Mutation.insert",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update",
            full_name="google.spanner.v1.Mutation.update",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="insert_or_update",
            full_name="google.spanner.v1.Mutation.insert_or_update",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="replace",
            full_name="google.spanner.v1.Mutation.replace",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="delete",
            full_name="google.spanner.v1.Mutation.delete",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_MUTATION_WRITE, _MUTATION_DELETE],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="operation",
            full_name="google.spanner.v1.Mutation.operation",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=170,
    serialized_end=624,
)

_MUTATION_WRITE.fields_by_name[
    "values"
].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_MUTATION_WRITE.containing_type = _MUTATION
_MUTATION_DELETE.fields_by_name[
    "key_set"
].message_type = google_dot_cloud_dot_spanner__v1_dot_proto_dot_keys__pb2._KEYSET
_MUTATION_DELETE.containing_type = _MUTATION
_MUTATION.fields_by_name["insert"].message_type = _MUTATION_WRITE
_MUTATION.fields_by_name["update"].message_type = _MUTATION_WRITE
_MUTATION.fields_by_name["insert_or_update"].message_type = _MUTATION_WRITE
_MUTATION.fields_by_name["replace"].message_type = _MUTATION_WRITE
_MUTATION.fields_by_name["delete"].message_type = _MUTATION_DELETE
_MUTATION.oneofs_by_name["operation"].fields.append(_MUTATION.fields_by_name["insert"])
_MUTATION.fields_by_name["insert"].containing_oneof = _MUTATION.oneofs_by_name[
    "operation"
]
_MUTATION.oneofs_by_name["operation"].fields.append(_MUTATION.fields_by_name["update"])
_MUTATION.fields_by_name["update"].containing_oneof = _MUTATION.oneofs_by_name[
    "operation"
]
_MUTATION.oneofs_by_name["operation"].fields.append(
    _MUTATION.fields_by_name["insert_or_update"]
)
_MUTATION.fields_by_name[
    "insert_or_update"
].containing_oneof = _MUTATION.oneofs_by_name["operation"]
_MUTATION.oneofs_by_name["operation"].fields.append(_MUTATION.fields_by_name["replace"])
_MUTATION.fields_by_name["replace"].containing_oneof = _MUTATION.oneofs_by_name[
    "operation"
]
_MUTATION.oneofs_by_name["operation"].fields.append(_MUTATION.fields_by_name["delete"])
_MUTATION.fields_by_name["delete"].containing_oneof = _MUTATION.oneofs_by_name[
    "operation"
]
DESCRIPTOR.message_types_by_name["Mutation"] = _MUTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Mutation = _reflection.GeneratedProtocolMessageType(
    "Mutation",
    (_message.Message,),
    {
        "Write": _reflection.GeneratedProtocolMessageType(
            "Write",
            (_message.Message,),
            {
                "DESCRIPTOR": _MUTATION_WRITE,
                "__module__": "google.cloud.spanner_v1.proto.mutation_pb2",
                "__doc__": """Arguments to [insert][google.spanner.v1.Mutation.insert],
    [update][google.spanner.v1.Mutation.update],
    [insert_or_update][google.spanner.v1.Mutation.insert_or_update], and
    [replace][google.spanner.v1.Mutation.replace] operations.
    Attributes:
        table:
            Required. The table whose rows will be written.
        columns:
            The names of the columns in
            [table][google.spanner.v1.Mutation.Write.table] to be written.
            The list of columns must contain enough columns to allow Cloud
            Spanner to derive values for all primary key columns in the
            row(s) to be modified.
        values:
            The values to be written. ``values`` can contain more than one
            list of values. If it does, then multiple rows are written,
            one for each entry in ``values``. Each list in ``values`` must
            have exactly as many entries as there are entries in
            [columns][google.spanner.v1.Mutation.Write.columns] above.
            Sending multiple lists is equivalent to sending multiple
            ``Mutation``\ s, each containing one ``values`` entry and
            repeating [table][google.spanner.v1.Mutation.Write.table] and
            [columns][google.spanner.v1.Mutation.Write.columns].
            Individual values in each list are encoded as described
            [here][google.spanner.v1.TypeCode].
    """,
                # @@protoc_insertion_point(class_scope:google.spanner.v1.Mutation.Write)
            },
        ),
        "Delete": _reflection.GeneratedProtocolMessageType(
            "Delete",
            (_message.Message,),
            {
                "DESCRIPTOR": _MUTATION_DELETE,
                "__module__": "google.cloud.spanner_v1.proto.mutation_pb2",
                "__doc__": """Arguments to [delete][google.spanner.v1.Mutation.delete] operations.
    Attributes:
        table:
            Required. The table whose rows will be deleted.
        key_set:
            Required. The primary keys of the rows within
            [table][google.spanner.v1.Mutation.Delete.table] to delete.
            The primary keys must be specified in the order in which they
            appear in the ``PRIMARY KEY()`` clause of the table’s
            equivalent DDL statement (the DDL statement used to create the
            table). Delete is idempotent. The transaction will succeed
            even if some or all rows do not exist.
    """,
                # @@protoc_insertion_point(class_scope:google.spanner.v1.Mutation.Delete)
            },
        ),
        "DESCRIPTOR": _MUTATION,
        "__module__": "google.cloud.spanner_v1.proto.mutation_pb2",
        "__doc__": """A modification to one or more Cloud Spanner rows. Mutations can be
  applied to a Cloud Spanner database by sending them in a
  [Commit][google.spanner.v1.Spanner.Commit] call.
  Attributes:
      operation:
          Required. The operation to perform.
      insert:
          Insert new rows in a table. If any of the rows already exist,
          the write or transaction fails with error ``ALREADY_EXISTS``.
      update:
          Update existing rows in a table. If any of the rows does not
          already exist, the transaction fails with error ``NOT_FOUND``.
      insert_or_update:
          Like [insert][google.spanner.v1.Mutation.insert], except that
          if the row already exists, then its column values are
          overwritten with the ones provided. Any column values not
          explicitly written are preserved.  When using [insert_or_updat
          e][google.spanner.v1.Mutation.insert_or_update], just as when
          using [insert][google.spanner.v1.Mutation.insert], all ``NOT
          NULL`` columns in the table must be given a value. This holds
          true even when the row already exists and will therefore
          actually be updated.
      replace:
          Like [insert][google.spanner.v1.Mutation.insert], except that
          if the row already exists, it is deleted, and the column
          values provided are inserted instead. Unlike [insert_or_update
          ][google.spanner.v1.Mutation.insert_or_update], this means any
          values not explicitly written become ``NULL``.  In an
          interleaved table, if you create the child table with the ``ON
          DELETE CASCADE`` annotation, then replacing a parent row also
          deletes the child rows. Otherwise, you must delete the child
          rows before you replace the parent row.
      delete:
          Delete rows from a table. Succeeds whether or not the named
          rows were present.
  """,
        # @@protoc_insertion_point(class_scope:google.spanner.v1.Mutation)
    },
)
_sym_db.RegisterMessage(Mutation)
_sym_db.RegisterMessage(Mutation.Write)
_sym_db.RegisterMessage(Mutation.Delete)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
