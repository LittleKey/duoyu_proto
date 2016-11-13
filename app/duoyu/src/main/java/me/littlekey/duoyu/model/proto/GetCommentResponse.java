// Code generated by Wire protocol buffer compiler, do not edit.
// Source file: business/comment.proto at 20:1
package me.littlekey.duoyu.model.proto;

import com.squareup.wire.FieldEncoding;
import com.squareup.wire.Message;
import com.squareup.wire.ProtoAdapter;
import com.squareup.wire.ProtoReader;
import com.squareup.wire.ProtoWriter;
import com.squareup.wire.WireField;
import com.squareup.wire.internal.Internal;
import java.io.IOException;
import java.lang.Object;
import java.lang.Override;
import java.lang.String;
import java.lang.StringBuilder;
import java.util.List;
import okio.ByteString;

public final class GetCommentResponse extends Message<GetCommentResponse, GetCommentResponse.Builder> {
  public static final ProtoAdapter<GetCommentResponse> ADAPTER = new ProtoAdapter_GetCommentResponse();

  private static final long serialVersionUID = 0L;

  @WireField(
      tag = 1,
      adapter = "me.littlekey.duoyu.model.proto.Comment#ADAPTER",
      label = WireField.Label.REPEATED
  )
  public final List<Comment> comments;

  @WireField(
      tag = 2,
      adapter = "me.littlekey.duoyu.model.proto.Cursor#ADAPTER"
  )
  public final Cursor cursor;

  public GetCommentResponse(List<Comment> comments, Cursor cursor) {
    this(comments, cursor, ByteString.EMPTY);
  }

  public GetCommentResponse(List<Comment> comments, Cursor cursor, ByteString unknownFields) {
    super(ADAPTER, unknownFields);
    this.comments = Internal.immutableCopyOf("comments", comments);
    this.cursor = cursor;
  }

  @Override
  public Builder newBuilder() {
    Builder builder = new Builder();
    builder.comments = Internal.copyOf("comments", comments);
    builder.cursor = cursor;
    builder.addUnknownFields(unknownFields());
    return builder;
  }

  @Override
  public boolean equals(Object other) {
    if (other == this) return true;
    if (!(other instanceof GetCommentResponse)) return false;
    GetCommentResponse o = (GetCommentResponse) other;
    return unknownFields().equals(o.unknownFields())
        && comments.equals(o.comments)
        && Internal.equals(cursor, o.cursor);
  }

  @Override
  public int hashCode() {
    int result = super.hashCode;
    if (result == 0) {
      result = unknownFields().hashCode();
      result = result * 37 + comments.hashCode();
      result = result * 37 + (cursor != null ? cursor.hashCode() : 0);
      super.hashCode = result;
    }
    return result;
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    if (!comments.isEmpty()) builder.append(", comments=").append(comments);
    if (cursor != null) builder.append(", cursor=").append(cursor);
    return builder.replace(0, 2, "GetCommentResponse{").append('}').toString();
  }

  public static final class Builder extends Message.Builder<GetCommentResponse, Builder> {
    public List<Comment> comments;

    public Cursor cursor;

    public Builder() {
      comments = Internal.newMutableList();
    }

    public Builder comments(List<Comment> comments) {
      Internal.checkElementsNotNull(comments);
      this.comments = comments;
      return this;
    }

    public Builder cursor(Cursor cursor) {
      this.cursor = cursor;
      return this;
    }

    @Override
    public GetCommentResponse build() {
      return new GetCommentResponse(comments, cursor, super.buildUnknownFields());
    }
  }

  private static final class ProtoAdapter_GetCommentResponse extends ProtoAdapter<GetCommentResponse> {
    ProtoAdapter_GetCommentResponse() {
      super(FieldEncoding.LENGTH_DELIMITED, GetCommentResponse.class);
    }

    @Override
    public int encodedSize(GetCommentResponse value) {
      return Comment.ADAPTER.asRepeated().encodedSizeWithTag(1, value.comments)
          + (value.cursor != null ? Cursor.ADAPTER.encodedSizeWithTag(2, value.cursor) : 0)
          + value.unknownFields().size();
    }

    @Override
    public void encode(ProtoWriter writer, GetCommentResponse value) throws IOException {
      Comment.ADAPTER.asRepeated().encodeWithTag(writer, 1, value.comments);
      if (value.cursor != null) Cursor.ADAPTER.encodeWithTag(writer, 2, value.cursor);
      writer.writeBytes(value.unknownFields());
    }

    @Override
    public GetCommentResponse decode(ProtoReader reader) throws IOException {
      Builder builder = new Builder();
      long token = reader.beginMessage();
      for (int tag; (tag = reader.nextTag()) != -1;) {
        switch (tag) {
          case 1: builder.comments.add(Comment.ADAPTER.decode(reader)); break;
          case 2: builder.cursor(Cursor.ADAPTER.decode(reader)); break;
          default: {
            FieldEncoding fieldEncoding = reader.peekFieldEncoding();
            Object value = fieldEncoding.rawProtoAdapter().decode(reader);
            builder.addUnknownField(tag, fieldEncoding, value);
          }
        }
      }
      reader.endMessage(token);
      return builder.build();
    }

    @Override
    public GetCommentResponse redact(GetCommentResponse value) {
      Builder builder = value.newBuilder();
      Internal.redactElements(builder.comments, Comment.ADAPTER);
      if (builder.cursor != null) builder.cursor = Cursor.ADAPTER.redact(builder.cursor);
      builder.clearUnknownFields();
      return builder.build();
    }
  }
}
